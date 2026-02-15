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
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const post_id = route.params.id

const title = ref('')
const text = ref('')

const loading = ref(true)
const saving = ref(false)
const message = ref('')

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
.title {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

/* Loading / empty */
.empty {
  display: flex;
  justify-content: center;
  padding: 30px;
}

/* Центр */
.update {
  display: flex;
  justify-content: center;
  padding: 20px;
}

/* Карточка */
.card {
  width: 100%;
  max-width: 520px;
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

/* Ошибка */
.error {
  color: #ff6b6b;
  font-size: 13px;
  text-align: center;
}

/* Ссылки */
.links {
  display: flex;
  justify-content: space-between;
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
