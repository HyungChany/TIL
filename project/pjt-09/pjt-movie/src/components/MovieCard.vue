<template>
  <div class="card" style="margin-top: 20px;">
    <RouterLink
      :to="{ name: 'MovieDetailView', params: { moviePk: movie.id } }">
      <div class="card-image">
        <img
          :src="getImageUrl(movie.poster_path)"
          alt="..."
        />
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
const props = defineProps(["movie"]);

const getImageUrl = (path) => {
  return path ? `https://image.tmdb.org/t/p/w500${path}` : "";
};
</script>

<style scoped>
/* .card-container {
  width: 100%;
  display: flex;
  justify-content: center;
} */

.card {
  position: relative;
  width: 18rem;
  height: 26rem;
  border-radius: 8px;
  overflow: hidden;
  margin: 0.5rem;
  transition: transform 0.3s;
}

.card:hover {
  box-shadow: 0 30px 50px 0 rgba(0, 0, 0, 0.779);
}

.card-image {
  position: relative;
  width: 100%;
  padding-bottom: 150%; /* 1:1 Aspect Ratio */
  overflow: hidden;
}

.card-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>