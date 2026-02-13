<template>
  <div class="page">

    <div class="card">

      <h1>Create account</h1>
      <p class="subtitle">Join Forgeswords today</p>

      <div class="form">

        <input
          type="text"
          v-model="name"
          placeholder="Username"
        />

        <input
          type="password"
          v-model="password"
          placeholder="Password"
        />

        <button @click="signup">
          Sign up
        </button>

      </div>

      <div class="links">
        <RouterLink to="/login">
          Already have an account?
        </RouterLink>

        <RouterLink to="/">
          ← Back home
        </RouterLink>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const router = useRouter()

const name = ref('')
const password = ref('')

async function signup() {
  if (!name.value || !password.value) {
    alert('Fill all fields')
    return
  }

  try {
    await api.post('/signup', {
      name: name.value,
      password: password.value
    })

    router.push('/login')
  } catch (err) {
    alert('Signup failed')
  }
}
</script>

<style scoped>
/* ===== ФОН ===== */

.page {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f172a, #1e293b);

  display: flex;
  align-items: center;
  justify-content: center;
}


/* ===== КАРТОЧКА ===== */

.card {
  background: #020617;
  color: white;

  width: 100%;
  max-width: 380px;

  padding: 35px 30px;
  border-radius: 14px;

  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}


/* ===== ЗАГОЛОВКИ ===== */

h1 {
  text-align: center;
  margin-bottom: 5px;
}

.subtitle {
  text-align: center;
  color: #94a3b8;
  font-size: 14px;
  margin-bottom: 25px;
}


/* ===== ФОРМА ===== */

.form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

input {
  background: #020617;
  border: 1px solid #1e293b;

  padding: 12px 14px;
  border-radius: 8px;

  color: white;
  font-size: 14px;

  outline: none;
  transition: 0.2s;
}

input:focus {
  border-color: #38bdf8;
  box-shadow: 0 0 0 1px #38bdf8;
}


/* ===== КНОПКА ===== */

button {
  margin-top: 5px;

  background: linear-gradient(135deg, #a855f7, #7c3aed);
  border: none;
  color: white;

  padding: 12px;
  border-radius: 8px;

  font-size: 15px;
  font-weight: 600;

  cursor: pointer;
  transition: 0.2s;
}

button:hover {
  transform: scale(1.03);
  opacity: 0.9;
}

button:active {
  transform: scale(0.98);
}


/* ===== ССЫЛКИ ===== */

.links {
  margin-top: 20px;

  display: flex;
  flex-direction: column;
  gap: 8px;

  text-align: center;
}

.links a {
  color: #94a3b8;
  text-decoration: none;
  font-size: 13px;

  transition: 0.2s;
}

.links a:hover {
  color: white;
}
</style>
