<template>
 <div class="main-content">
  <md-layout md-gutter>
   <md-layout md-gutter md-flex="20">
    <md-whiteframe md-elevation="5" style="width: 100%">
     <div>
      <h1>
       Content Organizer
      </h1>
      <ul class="md-list md-dense">
       <li class="md-list-item">Cylinder</li>
       <li class="md-list-item">Cube</li>
       <li class="md-list-item">Sphere</li>
       <li class="md-list-item">Map</li>
      </ul>
     </div>
    </md-whiteframe>
   </md-layout>
   <md-layout md-gutter>
    <a-scene>
     <a-box position="-1 -0.5 -3" rotation="0 45 0" color="#4CC3D9"
      event-set__enter="_event: mouseenter; color: #6FF7FF"
      event-set__leave="_event: mouseleave; color: #4CC3D9">
     </a-box>
     <a-sphere position="0 0.25 -5" radius="1.25" color="#EF2D5E"
      event-set__enter="_event: mouseenter; color: #FF4F8F"
      event-set__leave="_event: mouseleave; color: #EF2D5E">
     </a-sphere>
     <a-cylinder position="1 -0.25 -3" radius="0.5" height="1.5" color="#FFC65D"
      event-set__enter="_event: mouseenter; color: #FFE87F"
      event-set__leave="_event: mouseleave; color: #FFC65D">
     </a-cylinder>
     <a-plane position="0 -1 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
     <a-sky color="#ECECEC"></a-sky>
     <a-entity camera look-controls mouse-cursor></a-entity>
    </a-scene>
   </md-layout>
  </md-layout>
 </div>
</template>

<script>
  export default {
    data() {
      return {
	test: 5
      };
    },
    mounted() {
      var self = this;
      this.$wamp.call('com.example.add2', [2,2]).then(
        function(res) {
          self.test = res;
        }
      );
    }
  }
</script>
