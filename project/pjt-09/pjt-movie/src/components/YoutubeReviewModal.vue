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
          <!-- 큰따옴표와 같은 요소들 디코딩을 위한 v-html -->
          <h5
            class="modal-title"
            id="youtubeTrailerLabel"
            v-html="`${props.videoTitle} 리뷰 영상`"
          ></h5>
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
            v-else
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
import { ref, onMounted, onBeforeUnmount } from "vue";

const props = defineProps({
  videoTitle: String,
  currentVideoId: String,
});

const videoData = ref("");
const isLoading = ref(false);
const modalRef = ref(null);

const stopVideo = () => {
  videoData.value = "";
};

const fetchReview = () => {
  isLoading.value = true;
  try {
    videoData.value = `https://www.youtube.com/embed/${props.currentVideoId}?autoplay=1&mute=1`;
  } catch (error) {
    console.error("서버에러:", error);
  }
  isLoading.value = false;
};

onMounted(() => {
  if (modalRef.value) {
    modalRef.value.addEventListener("show.bs.modal", fetchReview);
  }
});

onBeforeUnmount(() => {
  if (modalRef.value) {
    modalRef.value.removeEventListener("show.bs.modal", fetchReview);
  }
});
</script>

<style scoped>
.modal-content {
  max-width: 820px;
}

.trailer-iframe {
  width: 720px;
  height: 450px;
  display: block;
  margin: 0 auto;
}
</style>
