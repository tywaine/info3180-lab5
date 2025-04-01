<script setup>
import {ref, onMounted} from "vue";

onMounted(() => {
  fetchMovies();
})

let movies = ref([])

function fetchMovies(){
  movies.value = []

  fetch('/api/v1/movies')
    .then((response) => response.json())
    .then((data) => {
      if(data.movies){
        movies.value = data.movies;
      }
      console.log(data);
  })
      .catch((error) => {
        console.error("Error fetching Movies:", error);
      });
}

</script>

<template>
  <div class="movies-container">
    <h1 class="page-header">Movies</h1>
    <div v-if="movies.length === 0">No movies available</div>

    <div v-else class="movies-list">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
        <div class="movie-info">
          <h2>{{ movie.title }}</h2>
          <p>{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.movies-container {
  max-width: 1550px;
  margin: auto;
  padding: 20px;
  text-align: center;
}

.page-header {
  margin-bottom: 20px;
}

.movies-list {
  display: flex;
  flex-wrap: wrap;
  gap: 75px;
  justify-content: center;
}

.movie-card {
  display: flex;
  background-color: white;
  color: black;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 615px;
  align-items: center;
}

.movie-poster {
  width: 250px;
  height: 300px;
  object-fit: cover;
  border-right: 3px solid #ddd;
}

.movie-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 15px;
  flex-grow: 1;
  text-align: left;
}

h2 {
  font-size: 18px;
  margin-bottom: 12px;
  align-self: flex-start;
}

p {
  font-size: 14px;
  color: #333;
  flex-grow: 1;
  display: flex;
  align-items: center;
}
</style>
