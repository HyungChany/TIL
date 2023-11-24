<template>
  <div class="movie-detail-container">
    <div class="movie-poster">
      <img :src="getImageUrl(movie.poster_path)" alt="..." />
    </div>
    <h1 class="movie-title">{{ movie.title }}</h1>
    <div class="movie-info">
      <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
      <p><strong>러닝타임:</strong> {{ movie.runtime }} 분</p>
      <p><strong>TMDB 평점:</strong> {{ movie.vote_average }}</p>
    </div>

    <h3 class="movie-titles">장르</h3>
    <div class="movie-info">
      <ul class="genre-list">
        <li v-for="genre in movie.genres" :key="genre.name">
          {{ genre.name }}
        </li>
      </ul>
    </div>

    <h3 class="movie-titles">줄거리</h3>
    <div class="movie-overview">
      <p>{{ movie.overview }}</p>
    </div>

    <div class="movie-youtube">
      <h3>공식 예고편</h3>
      <button
        type="button"
        class="btn"
        @click="openModal"
        data-bs-toggle="modal"
        data-bs-target="#youtubeTrailerModal"
      >
        <img src="@/assets/youtubeLogo.png" alt="youtube" class="youtube-logo" />
      </button>

      <YoutubeTrailerModal :movieTitle="movie.title" />
    </div>
  </div>
</template>

<script setup>
import youtubeLogo from "@/assets/youtubeLogo.png";
import YoutubeTrailerModal from "@/components/YoutubeTrailerModal.vue";
import { onMounted } from "vue";

const props = defineProps(["movie"]);

const getImageUrl = (path) => {
  // 이미지가 없는경우 예외처리
  if (!path) {
    return;
  }
  return `https://image.tmdb.org/t/p/w500${path}`;
};

onMounted(() => {
  getImageUrl();
});
</script>

<style scoped>
.movie-detail-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 5rem;
  color: lightgrey;
}

.movie-poster img {
  max-width: 300px;
  box-shadow: 0 5px 7px rgb(37, 2, 51);
}

.movie-title {
  margin-top: 20px;
  font-size: 35px;
  font-weight: bold;
}

.movie-titles {
  margin-top: 20px;
  font-size: 25px;
  font-weight: bold;
}

.movie-info {
  margin-top: 20px;
  text-align: center;
}

.movie-overview {
  margin-top: 20px;
  padding-left: 3rem;
  padding-right: 3rem;
  text-align: center;
}

.genre-list {
  display: flex;
  justify-content: center;
  gap: 15px;
  list-style-type: none;
  padding-left: 0;
}

.genre-list li {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
.youtube-logo {
  width: 36px;
  height: 36px;
}

.movie-youtube {
  margin-top: 20px;
  padding-left: 7rem;
  padding-right: 7rem;
  text-align: center;
  margin-bottom: 5rem;
}
</style>
