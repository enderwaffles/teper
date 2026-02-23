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
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()


//data
let title = ref('')
let text = ref('')
let file = ref(null)
let loading = ref(false)


//functions
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

</style>
