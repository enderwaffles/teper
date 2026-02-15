<template>
  <Header />

  <div class="title">
    <h1>Create post</h1>
  </div>

  <main class="create">
    <div class="card">

      <input v-model="title" placeholder="Title" />

      <textarea
        v-model="text"
        placeholder="Text"
        rows="5"
      ></textarea>

      <label class="file">
        Upload image
        <input type="file" @change="getFile" hidden />
      </label>

      <p v-if="file" class="filename">
        {{ file.name }}
      </p>

      <button :disabled="loading" @click="send">
        {{ loading ? 'Sending...' : 'Send' }}
      </button>

      <div class="links">
        <a href="#" @click.prevent="goBack">← Back</a>
      </div>

    </div>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const title = ref('')
const text = ref('')
const file = ref(null)
const loading = ref(false)

function getFile(e) {
  file.value = e.target.files?.[0] ?? null
}



async function send() {
  if (!title.value || !text.value) {
    alert('Fill in all fields')
    return
  }

  try {
    loading.value = true

    const form = new FormData()
    form.append('title', title.value)
    form.append('text', text.value)

    if (file.value) {
      form.append('file', file.value)
    }

    await api.post('/posts', form)
    router.push('/posts')
  } catch (err) {
    console.error(err)
    alert('Error while sending post')
  } finally {
    loading.value = false
  }
}

function goBack() {
  // если человек открыл страницу напрямую — отправим домой
  if (window.history.length > 1) router.back()
  else router.push('/')
}
</script>

<style scoped>
.title {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

/* Центр */
.create {
  display: flex;
  justify-content: center;
  padding: 20px;
}

/* Карточка */
.card {
  width: 100%;
  max-width: 500px;
  background-color: rgb(30, 30, 30);
  border-radius: 20px;
  padding: 24px;

  display: flex;
  flex-direction: column;
  gap: 14px;
}

/* Инпуты */
input,
textarea {
  background: rgb(20, 20, 20);
  border: 1px solid rgb(50, 50, 50);
  border-radius: 10px;
  padding: 10px 12px;
  color: rgb(200, 200, 200);
  font-size: 14px;
  resize: none;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: rgb(90, 90, 90);
}

/* Файл */
.file {
  background: rgb(40, 40, 40);
  border-radius: 10px;
  padding: 8px;
  text-align: center;
  cursor: pointer;
  font-size: 13px;
  color: rgb(180, 180, 180);
  transition: 0.2s;
}

.file:hover {
  background: rgb(60, 60, 60);
}

.filename {
  font-size: 12px;
  color: rgb(120, 120, 120);
  text-align: center;
}

/* Кнопка */
button {
  background: rgb(60, 60, 60);
  border: none;
  border-radius: 12px;
  padding: 10px;
  color: rgb(220, 220, 220);
  cursor: pointer;
  transition: 0.2s;
}

button:hover {
  background: rgb(80, 80, 80);
}

button:disabled {
  opacity: 0.6;
  cursor: default;
}

/* Back */
.links {
  display: flex;
  justify-content: start;
  font-size: 13px;
}

.links a {
  color: rgb(120, 120, 120);
  text-decoration: none;
}

.links a:hover {
  color: rgb(180, 180, 180);
}
</style>
