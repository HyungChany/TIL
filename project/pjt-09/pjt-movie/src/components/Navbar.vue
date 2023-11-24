<template>
  <nav style="background-color: lightgray;">
    <div class="navbar-content">
      <RouterLink to="/" class="logo" style="margin: ;">
        <img :src="logo" alt="Logo" height="60" />
      </RouterLink>

      <div class="welcome-text">
        <div ref="welcomeText"></div>
      </div>
      
      <div class="navba">
        <RouterLink to="/movies" active-class="active-tab"
          >영화조회</RouterLink>
        <p class="span">|</p>
        <RouterLink to="/review-search" active-class="active-tab"
          >영상검색</RouterLink>
        <p class="span">|</p>
        <RouterLink to="/recommended" active-class="active-tab"
          >영화추천</RouterLink>   
      </div>            
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import logoSrc from '@/assets/logo.png'
import TypeIt from 'typeit';

const logo = ref(logoSrc)

onMounted(() => {
  new TypeIt(document.querySelector('.welcome-text div'), {
    strings: ['Welcome Movie World!'],
    speed: 150,
    keyboard: true,
    lifeLike: true,
    waitUntilVisible: true,
    loop: true,
  }).go();
});
</script>

<style scoped>
.welcome-text {
  color: #372463;
  font-size: 20px;
  margin-right: 10px;
}
.active-tab {
  color: #372463 !important;
  font-weight: bold !important;
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
  margin: 0 10px;
}

.span {
 margin : 0 10px;
 font-weight: bold
}

.navba{
  display: flex;
  margin-right: 10px;
  
}
.navba a{
  color: #372463;
  text-decoration: none;
}

.navba a:hover {
  color: #372463;
  text-decoration: underline; 
}
</style>