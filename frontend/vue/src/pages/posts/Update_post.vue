<template>
  <Header />

  <div class="title">
    <h1>Update post</h1>
  </div>

  <!-- Loading -->
  <main v-if="loading" class="empty">
    <p>Loading...</p>
  </main>

  <!-- Form -->
  <main v-else class="update">
    <div class="card">

      <input
        v-model="title"
        placeholder="Title"
      />

      <textarea
        v-model="text"
        placeholder="Text"
        rows="6"
      ></textarea>

      <button
        :disabled="saving"
        @click="send"
      >
        {{ saving ? 'Saving...' : 'Save' }}
      </button>

      <p v-if="message" class="error">
        {{ message }}
      </p>

      <div class="links">
        <RouterLink :to="`/posts/${post_id}`">
          Back to post
        </RouterLink>

        <RouterLink to="/posts">
          Back to posts
        </RouterLink>
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
let post_id = route.params.id
let title = ref("")
let text = ref("")
let loading = ref(true)
let saving = ref(false)

let message = ref("")


//functions
onMounted(async () => {
  try {
    loading.value = true
    const res = await api.get(`/posts/${post_id}`)
    title.value = res.data.title ?? ''
    text.value = res.data.text ?? ''
  } catch (e) {
    console.error(e)
    message.value = 'Failed to load post'
  } finally {
    loading.value = false
  }
})

async function send() {
  if (!title.value || !text.value) {
    message.value = 'Fill in all fields'
    return
  }

  try {
    saving.value = true
    message.value = ''

    const form = new FormData()

    form.append('title', title.value)
    form.append('text', text.value)

    await api.patch(`/posts/${post_id}`, form)

    router.push(`/posts/${post_id}`)
  } catch (e) {
    console.error(e)
    message.value = 'Failed to update post'
  } finally {
    saving.value = false
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
