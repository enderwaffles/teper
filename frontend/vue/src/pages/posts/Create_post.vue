<template>
  <Header />

  <h1>Create post</h1>

  <input v-model="title" placeholder="Title" />
  <br>

  <input v-model="text" placeholder="Text" />
  <br>

  <input type="file" @change="getFile" />
  <br>

  <button @click="send">Send</button>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// данные
const title = ref('')
const text = ref('')
const file = ref(null)

// берём файл
function getFile(e) {
  file.value = e.target.files[0]
}

// отправка
async function send() {
  const form = new FormData()

  form.append('title', title.value)
  form.append('text', text.value)

  if (file.value) {
    form.append('file', file.value)
  }

  await api.post('/posts', form)

  router.push('/posts')
}
</script>
