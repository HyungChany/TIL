<script setup>
import Navbar from '@/components/Navbar.vue'


</script>

<template>
  <div class="app">
    <Navbar />
    <RouterView />
  </div>
</template>

<style>
body, .app {
  min-height: 100vh;
  margin: 0;
  padding: 0;
  background-color: #372463;
}
</style>
