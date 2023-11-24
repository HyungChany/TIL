<script setup>
import logo from '@/assets/home.png'
</script>

<template>
  <main>
    <img :src="logo" alt="Logo" class="centered-logo" />
  </main>
</template>

<style>
.centered-logo {
  display: block;
  margin: 0 auto;
  max-width: 70%; 
  height: auto; 
}
</style>
