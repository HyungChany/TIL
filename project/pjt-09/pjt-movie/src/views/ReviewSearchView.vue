<template>
  <div class="container">
    <div class="search-container">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="영화 제목을 검색해보세요"
        class="search-input"
        v-on:keyup.enter="searchReviews"
      />
      <button @click="searchReviews" class="search-button">검색</button>
    </div>

    <div v-if="showSearchResults" class="search-results">
      <div>"{{ searchQuery }}" 에 대한 검색 결과입니다.</div>
    </div>

    <div class="video-list">
      <div v-for="(video, index) in videos" :key="index" class="video-item">
        <YoutubeCard
          :thumbnail="video.snippet.thumbnails.default.url"
          :title="video.snippet.title"
          :descriptions="video.snippet.description"
          @click="openModal(index)"
        />
      </div>
    </div>

    <YoutubeTrailerModal
      :isModalOpen="isModalOpen"
      :movieTitle="title"
      :currentVideoId="currentVideoId"
      @closeModal="closeModal"
    />
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import YoutubeCard from "@/components/YoutubeCard.vue";
import YoutubeTrailerModal from "@/components/YoutubeTrailerModal.vue";

const searchQuery = ref("");
const videos = ref([]);
const currentVideoId = ref("");
const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY;
const title = ref("");
const showSearchResults = ref(false);
const isModalOpen = ref(false);

const searchReviews = () => {
  axios
    .get("https://www.googleapis.com/youtube/v3/search", {
      params: {
        part: "snippet",
        q: `영화 ${searchQuery.value} 리뷰`,
        key: youtubeKey,
        type: "video",
        maxResults: 10,
      },
    })
    .then((response) => {
      videos.value = response.data.items;
      showSearchResults.value = true;
    })
    .catch((error) => {
      console.error("API 호출 중 에러 발생:", error);
    });
};

const openModal = (index) => {
  const VideoId = videos.value[index].id.videoId;
  currentVideoId.value = VideoId;
  title.value = videos.value[index].snippet.title;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};
</script>

<style setup>
.container {
  width: 80%;
  margin: 0 auto;
  padding: 10px;
}

.search-container {
  display: flex;
  justify-content: center;
  margin: 2rem 0;
}

.search-input {
  width: 70%;
  padding: 12px;
  font-size: 1.1rem;
  border: none;
  border-radius: 4px;
}

.search-button {
  margin-left: 10px;
  padding: 10px 20px;
  font-size: 1.3rem;
  background-color: #e50914;
  color: bisque;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #b90006;
}

.search-results {
  margin: 0.5rem 0;
  padding: 0.5rem;
  font-size: 1.rem;
  color: lightgray;
}
</style>
