<template>
  <Header />

  <div class="title">
    <h1>Signup</h1>
  </div>

  <main class="auth">

    <div class="card">

      <input
        type="email"
        v-model="email"
        placeholder="Email"
      />

      <input
        type="text"
        v-model="nickname"
        placeholder="Nickname"
      />

      <input
        type="text"
        v-model="name"
        placeholder="Name"
      />

      <input
        type="text"
        v-model="surname"
        placeholder="Surname"
      />

      <input
        type="password"
        v-model="password"
        placeholder="Password"
      />

      <input
        type="password"
        v-model="repeat_password"
        placeholder="Repeat password"
      />

      <button
        :disabled="loading"
        @click="signup"
      >
        {{ loading ? 'Loading...' : 'Signup' }}
      </button>

      <p v-if="message" class="error">
        {{ message }}
      </p>

      <div class="links">
        <RouterLink to="/login">
          Already have an account?
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
import { useRouter } from 'vue-router'
import api from '@/api/api'

const router = useRouter()

const email = ref('')
const nickname = ref('')
const name = ref('')
const surname = ref('')
const password = ref('')
const repeat_password = ref('')

const message = ref('')
const loading = ref(false)

async function signup() {

  if (
    !email.value ||
    !nickname.value ||
    !name.value ||
    !surname.value ||
    !password.value ||
    !repeat_password.value
  ) {
    message.value = 'Fill in all fields'
    return
  }

  if (password.value !== repeat_password.value) {
    message.value = 'Passwords do not match'
    return
  }

  try {
    loading.value = true
    message.value = ''

    await api.post('/signup', {
      email: email.value,
      nickname: nickname.value,
      name: name.value,
      surname: surname.value,
      password: password.value
    })

    router.push('/login')
  }
  catch (error) {
    console.log(error)
    message.value = 'Signup failed'
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

/* Центрируем */
.auth {
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
  gap: 12px;
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

/* Ошибки */
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
