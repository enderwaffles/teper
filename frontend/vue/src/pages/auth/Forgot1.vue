<template>
    <Header />

    <div class="title">
        <h1>New password</h1>
    </div>

    <main class="auth">

        <div class="card">

            <input type="email" v-model="email" placeholder="Email" />
            <input type="new_password" v-model="new_password" placeholder="New password" />

            <button :disabled="loading" @click="send">
                {{ loading ? 'Loading...' : 'Change password' }}
            </button>

            <p v-if="message" class="error">
                {{ message }}
            </p>

            <div class="links">

            </div>

        </div>

    </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'
import api from '@/api/api'

const auth = useAuthStore()
const router = useRouter()
const route = useRoute()

const email = ref("")
const new_password = ref("")

const message = ref('')
const loading = ref(false)

async function send() {

    if(!email.value || !new_password) {
        message.value = "Fill all fields"
        return
    }


    try {
        loading.value = true
        message.value = ''

        const res = await api.post('/forgot1', {
            email: email.value,
            new_password: new_password.value
        })

        router.push(`/forgot2?email=${email.value}`)
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
