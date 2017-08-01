<template>
  <div id="app">
   <md-toolbar>
     <md-button class="md-icon-button" @click="$refs.leftSidenav.toggle()">
      <md-icon>menu</md-icon>
     </md-button>
     <h1 class="md-title toolbar-title">Mapthree</h1>
    <md-menu md-align-trigger md-direction="bottom left" ref="user-menu">
     <div md-menu-trigger>
      <md-avatar class="md-large">
       <img src="https://en.gravatar.com/userimage/66430581/ebff0f0734ce9f7a6d9d2dbee8eedafd.png" alt="Mark Murnane">
      </md-avatar>
      <b>Mark Murnane</b>
      <md-icon>expand_more</md-icon>
     </div>
     <md-menu-content>
      <md-avatar class="md-large">
       <img src="https://en.gravatar.com/userimage/66430581/ebff0f0734ce9f7a6d9d2dbee8eedafd.png" alt="Mark Murnane">
      </md-avatar>
      <span>Mark Murnane</span>
      <div>
       Spaces
       Things
       Models
       Textures
       Whatever else
       Probably change your password here, too.
      </div>
     </md-menu-content>
    </md-menu>
   </md-toolbar>
   <div class="main-content">
    <router-view></router-view>
   </div>
   <md-sidenav class="md-left" ref="leftSidenav">
    <md-toolbar class="md-large">
     <div class="md-toolbar-container">
      <h3 class="md-title">Menu</h3>
     </div>
    </md-toolbar>
    <router-link to="/"><h3>Home</h3></router-link>
    <router-link to="/space"><h3>Test Space</h3></router-link>
    <router-link to="/spaces"><h3>Spaces</h3></router-link>
    <router-link to="/contact"><h3>Contact</h3></router-link>
    <router-link to="/help"><h3>Help</h3></router-link>
   </md-sidenav>
  </div>
</template>

<script>
</script>

<style src="vue-material/dist/vue-material.css"></style>
<style>
.toolbar-title {
  flex-grow: 1;
}

.a-enter-vr-button {
  position: absolute;
  bottom: 65px;
  right: 0px;
}
</style>
