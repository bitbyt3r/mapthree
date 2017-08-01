<template>
  <div>
    <h1>Welcome to MapThree</h1>
    <h2>Spaces</h2>
    <ul class="md-list">
      <li v-for="space in spaces" :key="space.id" class="md-list-item">
        <router-link :to="'/space/' + space.id">
          <h3>{{ space.name }}</h3>
        </router-link>
        <p>{{ space.description }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        spaces: []
      };
    },
    mounted() {
      var self = this;
      this.$wamp.call('db.space.get_all').then(
        function(res) {
          self.spaces = res;
        }
      );
    }
  }
</script>
