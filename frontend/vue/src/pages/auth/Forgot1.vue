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
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()


//data
let email = ref("")
let new_password = ref("")
let message = ref('')
let loading = ref(false)


//functions
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

</style>
