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
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const route = useRoute()
const router = useRouter()
const auth = useAuthStore()

const post = ref(null)
const post_id = route.params.id
const comment = ref('')

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
.page {
  padding: 20px;
}

.wrap {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.card {
  background: rgb(30, 30, 30);
  border-radius: 18px;
  padding: 16px;
}

.top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.title {
  margin: 0;
  font-size: 22px;
  color: rgb(230, 230, 230);
}

.meta {
  margin-top: 8px;
  display: flex;
  gap: 12px;
  align-items: center;
  color: rgb(140, 140, 140);
  font-size: 13px;
}

.text {
  margin: 14px 0 0;
  color: rgb(200, 200, 200);
  line-height: 1.5;
}

.img {
  margin-top: 12px;
  width: 100%;
  max-height: 420px;
  object-fit: cover;
  border-radius: 14px;
  display: block;
}

.actions {
  display: flex;
  gap: 10px;
}

.btn {
  background: rgb(50, 50, 50);
  color: rgb(230, 230, 230);
  border: 0;
  padding: 8px 12px;
  border-radius: 10px;
  text-decoration: none;
  cursor: pointer;
  transition: 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.btn:hover {
  background: rgb(65, 65, 65);
}

.btn:disabled {
  opacity: 0.6;
  cursor: default;
}

.danger {
  background: rgb(90, 40, 40);
}

.danger:hover {
  background: rgb(120, 45, 45);
}

.small {
  padding: 6px 10px;
  border-radius: 9px;
  font-size: 12px;
}

.h2 {
  margin: 0 0 10px;
  color: rgb(230, 230, 230);
  font-size: 18px;
}

.comments {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.comment {
  background: rgb(40, 40, 40);
  border-radius: 14px;
  padding: 12px;
}

.comment_top {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  align-items: center;
}

.comment_author {
  color: rgb(210, 210, 210);
  font-size: 14px;
}

.comment_right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.comment_date {
  color: rgb(140, 140, 140);
  font-size: 12px;
}

.comment_text {
  margin-top: 8px;
  color: rgb(200, 200, 200);
  line-height: 1.45;
}

.hr {
  height: 1px;
  background: rgb(55, 55, 55);
  margin: 14px 0;
}

.write {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.write_top {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.me {
  color: rgb(210, 210, 210);
}

.write_row {
  display: flex;
  gap: 10px;
}

.input {
  flex: 1;
  background: rgb(40, 40, 40);
  border: 1px solid rgb(60, 60, 60);
  color: rgb(230, 230, 230);
  padding: 10px 12px;
  border-radius: 12px;
  outline: none;
}

.input:focus {
  border-color: rgb(90, 90, 90);
}

.muted {
  color: rgb(140, 140, 140);
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
