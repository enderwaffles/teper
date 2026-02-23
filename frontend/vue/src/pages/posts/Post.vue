<template>
  <Header />

  <div class="page">
    <div class="wrap" v-if="post">
      <!-- Post -->
      <div class="links">
        <a href="#" @click.prevent="goBack">← Back</a>
      </div>
      <div class="card">
        <div class="top">
          <h1 class="title">{{ post.title }}</h1>

          <div class="actions" v-if="auth.user && auth.user.id === post.author?.id || auth.user.admin">
            <RouterLink class="btn" :to="`/update_post/${post_id}`">Update</RouterLink>
            <button class="btn danger" type="button" @click="delete_post">Delete</button>
          </div>
        </div>

        <div class="meta">
          <span class="author">by {{ post.author?.email }}</span>
          <span v-if="post.date" class="date">{{ new Date(post.date).toLocaleString('ru-RU') }}</span>
        </div>

        <p class="text" v-if="post.text">{{ post.text }}</p>

        <img v-if="post.upload_url" class="img" :src="api.defaults.baseURL + post.upload_url" alt="" />
      </div>

      <!-- Comments -->
      <div class="card">
        <h2 class="h2">Comments</h2>

        <div v-if="sortedComments.length" class="comments">
          <div class="comment" v-for="c in sortedComments" :key="c.id">
            <div class="comment_top">
              <div class="comment_author">{{ c.author?.email }}</div>
              <div class="comment_right">
                <div v-if="c.date || c.created_at || c.createdAt" class="comment_date">
                  {{ commentDate(c) }}
                </div>

                <button v-if="auth.user && auth.user.id === c.author?.id || auth.user.admin" class="btn small danger" type="button"
                  @click="delete_comment(c.id)">
                  Delete
                </button>
              </div>
            </div>

            <div class="comment_text">{{ c.text }}</div>
          </div>
        </div>

        <p v-else class="muted">No comments yet</p>

        <div class="hr"></div>

        <!-- Write comment -->
        <div v-if="auth.user" class="write">
          <div class="write_top">
            <div class="muted">Write comment as</div>
            <div class="me">{{ auth.user.name }}</div>
          </div>

          <div class="write_row">
            <input class="input" type="text" v-model="comment" placeholder="comment" />
            <button class="btn" type="button" @click="send_comment" :disabled="!comment.trim()">
              Send
            </button>
          </div>
        </div>

        <p v-else class="muted">Login to comment</p>
      </div>
    </div>

    <div v-else class="wrap">
      <p class="muted">Loading...</p>
    </div>
  </div>
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
let post = ref(null)
let post_id = route.params.id
let comment = ref('')


//functions
onMounted(async () => {
  const res = await api.get(`/posts/${post_id}`)
  post.value = res.data
})

const sortedComments = computed(() => {
  if (!post.value?.comments) return []

  // сортируем по времени если есть поля даты
  return [...post.value.comments].sort((a, b) => {
    const da = new Date(a.date || a.created_at || a.createdAt || 0).getTime()
    const db = new Date(b.date || b.created_at || b.createdAt || 0).getTime()
    return db - da
  })
})

function commentDate(c) {
  const d = c.date || c.created_at || c.createdAt
  if (!d) return ''
  return new Date(d).toLocaleString('ru-RU')
}

async function delete_post() {
  await api.delete(`/posts/${post_id}`)
  router.push('/posts')
}

// comments
async function send_comment() {
  if (!comment.value.trim()) return

  const form = new FormData()
  form.append('text', comment.value)

  const res = await api.post(`/posts/comments/${post_id}`, form)

  // добавляем сразу в список
  post.value.comments.push(res.data)
  comment.value = ''
}

async function delete_comment(comment_id) {
  await api.delete(`/posts/comments/${comment_id}`)
  post.value.comments = post.value.comments.filter(c => c.id !== comment_id)
}

function goBack() {
  // если человек открыл страницу напрямую — отправим домой
  if (window.history.length > 1) router.back()
  else router.push('/')
}
</script>


<style scoped>

</style>
