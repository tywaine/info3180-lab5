<script setup>
import {ref, onMounted} from "vue";

onMounted(() => {
  getCsrfToken();
})

let csrf_token = ref("");
let successMessage = ref("");
let errorMessage = ref([]);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      csrf_token.value = data.csrf_token;
  })
      .catch((error) => {
        console.error("Error fetching CSRF token:", error);
      });
}

function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);

  successMessage.value = "";
  errorMessage.value = [];

  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    if (data.message) {
        successMessage.value = data.message;
        errorMessage.value = [];
        movieForm.reset();
    }
    if (data.errors) {
        successMessage.value = "";
        errorMessage.value = data.errors;
    }

    console.log(data);
  })
  .catch(function (error) {
    successMessage.value = "";
    errorMessage.value = ["An error occurred. Please try again."];
    console.error(error);
  });
}


</script>

<template>
  <h1 class="page-header">Create Movie</h1>

  <!-- Success Message -->
  <div v-if="successMessage" class="alert alert-success">
    {{ successMessage }}
  </div>

  <!-- Error Messages -->
  <div v-if="errorMessage.length" class="alert alert-danger">
    <ul>
      <li v-for="(error, index) in errorMessage" :key="index">
        {{ error }}
      </li>
    </ul>
  </div>

  <form @submit.prevent="saveMovie" id="movieForm">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" />
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" class="form-control" />
    </div>

    <button type="submit" name="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<style scoped>
.alert {
  padding: 10px;
  margin-bottom: 15px;
  border-radius: 5px;
}
.alert-success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}
.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
</style>