<template>
    <Header />

    <div>
        <h1>Reset password</h1>
    </div>

    <div>
        <p>We sent to your email code</p>
    </div>

    <div>
        <input type="incode" v-model="incode" placeholder="Code" />
        
        <button :disabled="loading" @click="reset">{{ loading ? 'Loading...' : 'Reset' }}</button>
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
const email = ref(route.query.email || "")

var incode = ref("")

let message = ref("")
let loading = ref(false)


//functions
async function reset() {

    if (!incode.value) {
        message.value = 'Fill in all fields'
        return
    }

    try {
        loading.value = true
        message.value = ''

        const res = await api.post('/forgot2', {
            email: email.value,
            code: incode.value
        })
        console.log(res)
        if (res.status == 200) {
            auth.login(res.data.user)

            router.push('/')
        }
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
