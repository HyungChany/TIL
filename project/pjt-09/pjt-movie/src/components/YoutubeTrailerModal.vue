<template>
  <div
    ref="modalRef"
    class="modal fade"
    id="youtubeTrailerModal"
    tabindex="-1"
    aria-labelledby="youtubeTrailerLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="youtubeTrailerLabel">
            {{ movieTitle }} 공식 예고편
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            @click="stopVideo"
          ></button>
        </div>
        <div class="modal-body">
          <div
            v-if="isLoading"
            class="spinner-border text-primary"
            role="status"
          >
            <span class="visually-hidden">Loading...</span>
          </div>
          <iframe
            v-else-if="videoData"
            class="trailer-iframe"
            :src="videoData"
            frameborder="0"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, defineProps, defineEmits, watch, ref } from "vue";
import axios from "axios";

const props = defineProps(["movieTitle", "isModalOpen"]);
const emits = defineEmits(["closeModal"]);

const videoData = ref("");
const isLoading = ref(false);
const modalRef = ref(null);
const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY;

const stopVideo = () => {
  videoData.value = "";
};

const fetchTrailer = () => {
  isLoading.value = true;
  const baseURL = "https://www.googleapis.com/youtube/v3/search";
  axios
    .get(baseURL, {
      params: {
        key: youtubeKey,
        part: "snippet",
        type: "video",
        q: props.movieTitle + "공식 예고편",
        maxResults: 1,
      },
    })
    .then((response) => {
      const videoId = response.data.items[0].id.videoId;
      videoData.value = `https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1`;
    })
    .catch((error) => {
      console.error("서버에러:", error);
    });
  isLoading.value = false;
};

onMounted(() => {
  if (modalRef.value) {
    modalRef.value.addEventListener("show.bs.modal", fetchTrailer);
  }
});

onBeforeUnmount(() => {
  if (modalRef.value) {
    modalRef.value.removeEventListener("show.bs.modal", fetchTrailer);
  }
});

watch(
  () => props.isModalOpen,
  (newValue, oldValue) => {
    if (newValue) {
      fetchTrailer();
    }
  }
);

watch(
  () => props.movieTitle,
  () => {
    fetchTrailer();
  }
);
</script>

<style scoped>
.trailer-iframe {
  width: 100%;
  height: 70vh;
  max-width: 100%;
}
.modal-dialog {
  width: 70vw;
}

.modal-title {
  color: #372463; 
  font-weight: bold;
}
</style>
