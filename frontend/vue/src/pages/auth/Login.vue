<template>
  <Header />

  <div class="title">
    <h1>Login</h1>
  </div>

  <main class="auth">

    <div class="card">

      <input type="email" v-model="email" placeholder="Email" />

      <input type="password" v-model="password" placeholder="Password" />

      <button :disabled="loading" @click="login">
        {{ loading ? 'Loading...' : 'Login' }}
      </button>

      <p v-if="message" class="error">
        {{ message }} <br>

        <div class="links">
          <RouterLink to="/forgot1">Forget password?</RouterLink>
        </div>
        
      </p>

      <div class="links">
        <RouterLink to="/signup">
          Don't have an account?
        </RouterLink>

        <RouterLink to="/">
          Back to home
        </RouterLink>
      </div>

    </div>

  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()

const email = ref('')
const password = ref('')

const message = ref('')
const loading = ref(false)

async function login() {
  if (!email.value || !password.value) {
    message.value = 'Fill in all fields'
    return
  }

  try {
    loading.value = true
    message.value = ''

    const res = await api.post('/login', {
      email: email.value,
      password: password.value
    })

    auth.login({
      id: res.data.user.id,
      email: res.data.user.email,
      nickname: res.data.user.nickname,
      name: res.data.user.name,
      surname: res.data.user.surname,

    })

    router.push('/')
  }
  catch (error) {
    console.log(error)
    message.value = 'Login failed'
  }
  finally {
    loading.value = false
  }
}
</script>

<style scoped>
.title {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

/* Центрируем форму */
.auth {
  display: flex;
  justify-content: center;
  padding: 20px;
}

/* Карточка */
.card {
  width: 100%;
  max-width: 400px;
  background-color: rgb(30, 30, 30);
  border-radius: 20px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

/* Инпуты */
input {
  background: rgb(20, 20, 20);
  border: 1px solid rgb(50, 50, 50);
  border-radius: 10px;
  padding: 10px 12px;
  color: rgb(200, 200, 200);
  font-size: 14px;
}

input:focus {
  outline: none;
  border-color: rgb(90, 90, 90);
}

/* Кнопка */
button {
  background: rgb(50, 50, 50);
  border: none;
  border-radius: 12px;
  padding: 10px;
  color: rgb(220, 220, 220);
  font-size: 14px;
  cursor: pointer;
  transition: 0.2s;
}

button:hover {
  background: rgb(70, 70, 70);
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
