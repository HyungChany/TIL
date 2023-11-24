<template>
  <div class="detail-container" v-if="movie">
    <MovieDetailInfo :movie="movie" />
  </div>
</template>

<script setup>
import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const key = import.meta.env.VITE_TMDB_API_KEY;
const route = useRoute();
const moviePk = route.params.moviePk;

const movie = ref({});

const fetchMovieDetail = (moviePk) => {
  const url = `https://api.themoviedb.org/3/movie/${moviePk}?language=ko-KR`;
  const headers = {
    accept: 'application/json',
    Authorization: `Bearer ${key}`
  }

  axios
    .get(url, { headers })
    .then((response) => {
      movie.value = response.data;
    })
    .catch((err) => {
      alert(err.message);
      console.log(err);
    })
}

onMounted(() => {
  fetchMovieDetail(moviePk);
})
</script>


<style scoped>
.detail-container {
  width: 60%;
  margin: 0 auto;
}
</style>