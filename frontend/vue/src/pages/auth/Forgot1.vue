<template>
    <Header />

    <div>
        <h1>New password</h1>
    </div>

    <div>
        <input type="email" v-model="email" placeholder="Email" /> <br>
        <input type="new_password" v-model="new_password" placeholder="New password" /> <br>

        <button :disabled="loading" @click="send">{{ loading ? 'Loading...' : 'Reset password' }}</button> <br>
        <p v-if="message" class="error">{{ message }}</p>
    </div>

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
var email = ref("")
var new_password = ref("")

let message = ref("")
let loading = ref(false)


//functions
async function send() {

    try {
        loading.value = true
        message.value = ""

        const res = await api.post('/forgot1', {
            email: email.value,
            new_password: new_password.value
        })

        router.push(`/forgot2?email=${email.value}`)

    }
    catch (error) {
        console.log(error)
        message.value = "Reset failed"
    }
    finally {
        loading.value = false
    }
}

</script>


<style scoped>

</style>
