<script setup>
import { ref, onMounted } from 'vue'
import api from './api'

import LoginForm from './LoginForm.vue'
import SignupForm from './SignupForm.vue'

const isAuthed = ref(false)
const view = ref('menu') // menu | login | signup

async function checkAuth() {
  try {
    await api.get('/protected')
    isAuthed.value = true
    view.value = 'authed'
  } catch {
    isAuthed.value = false
    view.value = 'menu'
  }
}

onMounted(checkAuth)

async function logout() {
  await api.post('/logout')
  isAuthed.value = false
  view.value = 'menu'
}
</script>

<template>
  <div>
    <!-- ЕСЛИ АВТОРИЗОВАН -->
    <div v-if="isAuthed">
      <button @click="logout">Logout</button>
    </div>

    <!-- ЕСЛИ НЕ АВТОРИЗОВАН -->
    <div v-else>
      <!-- МЕНЮ -->
      <div v-if="view === 'menu'">
        <button @click="view = 'login'">Login</button>
        <button @click="view = 'signup'">Signup</button>
      </div>

      <!-- ФОРМА ЛОГИНА -->
      <LoginForm
        v-else-if="view === 'login'"
        @success="checkAuth"
        @back="view = 'menu'"
      />

      <!-- ФОРМА РЕГИСТРАЦИИ -->
      <SignupForm
        v-else-if="view === 'signup'"
        @back="view = 'menu'"
        @done="view = 'login'"
      />
    </div>
  </div>
</template>
