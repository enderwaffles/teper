<template>
<<<<<<< HEAD
  <Header />

  <main class="page">
    <section class="auth">
      <div class="card">
        <header class="card__head">
          <p class="kicker">Account</p>
          <h1 class="title">Welcome back</h1>
          <p class="subtitle">Login to your account</p>
        </header>

        <div class="form">
          <label class="field">
            <span class="field__label">Username</span>
            <input
              class="input"
              type="text"
              v-model="name"
              placeholder="Enter your username"
              autocomplete="username"
            />
          </label>

          <label class="field">
            <span class="field__label">Password</span>
            <input
              class="input"
              type="password"
              v-model="password"
              placeholder="Enter your password"
              autocomplete="current-password"
            />
          </label>

          <p v-if="error" class="error" role="alert">
            {{ error }}
          </p>

          <button class="btn btn--primary" type="button" @click="login" :disabled="loading">
            {{ loading ? "Signing in…" : "Login" }}
          </button>

          <div class="links">
            <RouterLink class="link" to="/signup">Don’t have an account? <span class="link__accent">Sign up</span></RouterLink>
            <RouterLink class="link link--muted" to="/">← Back home</RouterLink>
          </div>
        </div>
      </div>

      <!-- Right side visual (desktop) -->
      <aside class="side" aria-hidden="true">
        <div class="orb orb--one"></div>
        <div class="orb orb--two"></div>
        <div class="side__glass"></div>
      </aside>
    </section>
  </main>
=======
<h1>Login</h1>

<input type="text" v-model="email" placeholder="email">
<input type="text" v-model="password" placeholder="password">
<button type="button" v-on:click="login()">Login</button>
<p>{{ message }}</p>
<RouterLink to="/signup">Don't have an account? </RouterLink>
<RouterLink to="/">Back to home </RouterLink>

>>>>>>> 6d13676
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()

const email = ref("")
const password = ref("")

const message = ref("")

const loading = ref(false)
const error = ref('')

async function login() {
<<<<<<< HEAD
  error.value = ''

  if (!name.value.trim() || !password.value) {
    error.value = 'Please fill in both fields.'
=======
  if (!email.value || !password.value) {
    alert('Fill all fields')
>>>>>>> 6d13676
    return
  }

  try {
    loading.value = true

    const res = await api.post('/login', {
<<<<<<< HEAD
      name: name.value.trim(),
=======
      email: email.value,
>>>>>>> 6d13676
      password: password.value
    })

    auth.login({
      id: res.data.user.id,
      name: res.data.user.name
    })

    router.push('/')
<<<<<<< HEAD
  } catch (e) {
    error.value = 'Login failed. Check your credentials and try again.'
  } finally {
    loading.value = false
=======
  } 
  catch (error) {
    alert('Login failed')
    console.log(error)
    message.value = error
>>>>>>> 6d13676
  }
}
</script>

<<<<<<< HEAD
<style scoped>
/* Same global page language */
.page {
  min-height: calc(100vh - 64px);
  padding: 32px 20px;

  background:
    radial-gradient(900px 500px at 10% 0%, rgba(255, 127, 80, 0.12), transparent 60%),
    radial-gradient(800px 500px at 90% 10%, rgba(139, 92, 246, 0.12), transparent 60%),
    #0b0b0f;
}

.auth {
  max-width: 1100px;
  margin: 0 auto;

  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  align-items: stretch;
}

@media (max-width: 900px) {
  .auth {
    grid-template-columns: 1fr;
  }
}

/* Card */
.card {
  border-radius: 22px;
  padding: 18px;

  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);

  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.card__head {
  padding: 6px 6px 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  margin-bottom: 14px;
}

.kicker {
  margin: 0;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.title {
  margin: 10px 0 0;
  font-size: 26px;
  font-weight: 950;
  color: rgba(255, 255, 255, 0.92);
  letter-spacing: 0.2px;
}

.subtitle {
  margin: 8px 0 0;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.68);
}

/* Form */
.form {
  padding: 6px;
  display: grid;
  gap: 12px;
}

.field {
  display: grid;
  gap: 8px;
}

.field__label {
  font-size: 13px;
  font-weight: 800;
  color: rgba(255, 255, 255, 0.78);
}

/* Inputs */
.input {
  width: 100%;
  padding: 12px 12px;
  border-radius: 14px;

  color: rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.10);

  outline: none;
  transition: box-shadow 180ms ease, border-color 180ms ease, background 180ms ease;
}

.input::placeholder {
  color: rgba(255, 255, 255, 0.45);
}

.input:focus {
  border-color: rgba(255, 127, 80, 0.35);
  box-shadow: 0 0 0 4px rgba(255, 127, 80, 0.14);
  background: rgba(255, 255, 255, 0.04);
}

/* Error */
.error {
  margin: 2px 0 0;
  padding: 10px 12px;
  border-radius: 14px;

  color: rgba(255, 255, 255, 0.92);
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid rgba(239, 68, 68, 0.22);
  font-weight: 800;
  font-size: 13px;
}

/* Buttons (same system) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;

  padding: 12px 14px;
  border-radius: 14px;

  font-weight: 900;
  font-size: 14px;

  border: 1px solid transparent;
  cursor: pointer;
  user-select: none;

  transition: transform 180ms ease, background 180ms ease, box-shadow 180ms ease, opacity 180ms ease;
}

.btn:active {
  transform: translateY(1px);
}

.btn:disabled {
  opacity: 0.55;
  cursor: not-allowed;
  transform: none;
}

.btn--primary {
  color: #fff;
  background: linear-gradient(135deg, #ff7f50, #8b5cf6);
  box-shadow: 0 12px 26px rgba(255, 127, 80, 0.18);
}

.btn--primary:hover {
  box-shadow: 0 16px 34px rgba(255, 127, 80, 0.24);
}

/* Links */
.links {
  margin-top: 2px;
  display: grid;
  gap: 8px;
  text-align: center;
}

.link {
  text-decoration: none;
  font-weight: 800;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.78);
  transition: color 180ms ease;
}

.link:hover {
  color: rgba(255, 255, 255, 0.92);
}

.link--muted {
  color: rgba(255, 255, 255, 0.62);
}

.link__accent {
  color: rgba(255, 127, 80, 0.92);
}

/* Right side visual */
.side {
  position: relative;
  border-radius: 22px;
  overflow: hidden;

  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.03);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.35);

  display: block;
}

@media (max-width: 900px) {
  .side {
    display: none;
  }
}

.side__glass {
  position: absolute;
  inset: 18px;
  border-radius: 26px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(18px);
  box-shadow: 0 30px 70px rgba(0, 0, 0, 0.5);
}

/* orbs */
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
}

.orb--one {
  width: 280px;
  height: 280px;
  background: #ff7f50;
  top: 40px;
  left: 40px;
}

.orb--two {
  width: 340px;
  height: 340px;
  background: #8b5cf6;
  bottom: 30px;
  right: 30px;
}
</style>
=======
<style scoped></style>
>>>>>>> 6d13676
