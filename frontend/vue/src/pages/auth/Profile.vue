<template>
  <Header />

  <div class="title">
    <h1>Profile</h1>
  </div>

  <main class="profile">

    <div class="card">

      <p><b>Email:</b> {{ auth.user?.email }}</p>
      <p><b>Nickname:</b> {{ auth.user?.nickname }}</p>
      <p><b>Name:</b> {{ auth.user?.name }}</p>
      <p><b>Surname:</b> {{ auth.user?.surname }}</p>

      <button @click="logout">
        Logout
      </button>
      
      <div class="links">
        <a href="#" @click.prevent="goBack">← Back</a>
      </div>
    </div>

  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const auth = useAuthStore()
const router = useRouter()

function logout() {
  auth.logout()
  router.push('/')
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
.profile {
  display: flex;
  justify-content: center;
  padding: 20px;
}

/* Карточка */
.card {
  width: 100%;
  max-width: 420px;
  background-color: rgb(30, 30, 30);
  border-radius: 20px;
  padding: 24px;

  display: flex;
  flex-direction: column;
  gap: 14px;
}

/* Текст */
p {
  color: rgb(200, 200, 200);
  font-size: 14px;
  margin: 0;
}

b {
  color: rgb(140, 140, 140);
  font-weight: normal;
}

/* Кнопка */
button {
  margin-top: 10px;
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

/* Ссылки */
.links {
  display: flex;
  justify-content: center;
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
