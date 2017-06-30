<template>
  <div>
    2+2={{ test }}
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
