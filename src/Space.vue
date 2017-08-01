<template>
 <div class="main-content">
  <md-layout md-gutter>
   <md-layout md-gutter md-flex="20">
    <md-whiteframe md-elevation="5" style="width: 100%">
     <div class="content-organizer">
      <h1>
       Content Organizer
      </h1>
      <ul class="md-list md-dense">
       <li v-for="entity in entities" :key="entity.id" class="md-list-item entity-list-item" v-on:click="lookAt(entity)">{{ entity.name }}</li>
      </ul>
     </div>
    </md-whiteframe>
   </md-layout>
   <md-layout md-gutter>
    <a-scene>
     <a-entity v-for="entity in entities" :key="entity.id" :id="entity.id" geometry="primitive: box" :position="entity.strpos">
     </a-entity>
     <a-text v-for="entity in entities" :key="entity.id" :id="entity.id" width="10" z-offset="2" anchor="center" color="black" :value="entity.text" :position="entity.strpos" billboard></a-text>
     <a-sky color="#ECECEC"></a-sky>
     <a-entity position="5 0 0" camera mouse-cursor look-controls="reverseMouseDrag: true" wasd-controls="fly: true">
     </a-entity>
    </a-scene>
   </md-layout>
  </md-layout>
 </div>
</template>

<style>
.entity-list-item:hover {
  background-color: blue;
  color: white;
  cursor: pointer;
};

.content-organizer {
  overflow-y: auto;
  height: 90vh;
};
</style>

<script>
  export default {
    data() {
      return {
	entities: []
      };
    },
    mounted() {
      var self = this;
      self.queries = [];
      self.$wamp.call('db.space.get', [], {"id": self.$route.params.id}).then(
        function(res) {
          self.space = res[0];
          self.$wamp.call('db.arrangement.get', [], {"space_id": self.space.id}).then(
            function(arrangements) {
              arrangements.forEach(function(arrangement) {
                self.$wamp.call('db.query.get', [], {"id": arrangement.query_id}).then(
                  function(query) {
                    self.queries.push(query[0]);
                    self.run_query(query[0]);
                  }
                );
              });
            }
          );
        }
      );
    },
    methods: {
      run_query: function(query) {
        var self = this;
        this.$wamp.call('run_query', [query.querystring]).then(
          function(res) {
            self.entities = JSON.parse(res).result;
            self.entities.forEach(function(entity) {
              entity.strpos = entity.pos[0] + " " + entity.pos[1] + " " + entity.pos[2];
            });
            document.querySelectorAll('a-entity').forEach(
              function(entity) {
                entity.addEventListener('click', function (evt) {
                  console.log(evt);
                  if (evt.detail.target.id) {
                    self.entities.forEach(function(ent) {
                      if (ent.id == evt.detail.target.id) {
                        self.lookAt(ent);
                      };
                    });
                  };
                });
              }
            );
          }
        );
      },
      lookAt: function(entity) {
        var camera = document.querySelector('a-entity[camera]');
        var anim = document.createElement("a-animation");
        var cam_pos = camera.object3D.position.clone();
        var entity_pos = new THREE.Vector3(...entity.pos);
        var to_vec = entity_pos.sub(cam_pos);
        var flat_dist = Math.sqrt(to_vec.x**2 + to_vec.z**2);
        var dest_x = 57.29*Math.atan2(to_vec.y, flat_dist);
        var dest_y = 57.29*Math.atan2(-1*to_vec.x, -1*to_vec.z);
        var dest = dest_x + " " + dest_y + " 0";
        var dist = to_vec.length();
        if (dist > 10) {
          var truck_anim = document.createElement("a-animation");
          truck_anim.setAttribute("attribute", "position");
          to_vec.normalize();
          to_vec.multiplyScalar(dist - 10);
          cam_pos.add(to_vec);
          truck_anim.setAttribute("to", cam_pos.x + " " + cam_pos.y + " " + cam_pos.z);
          truck_anim.setAttribute("dur", 1000);
          camera.appendChild(truck_anim);
        }
        anim.setAttribute("delay", 200);
        anim.setAttribute("dur", 600);
        anim.setAttribute("to", dest);
        anim.setAttribute("attribute", "rotation");
        camera.appendChild(anim);
      }
    }
  }
</script>
