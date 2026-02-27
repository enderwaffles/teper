<template>
    <Header />

    <div>
        <h1>Chat</h1>
    </div>
    
    <div v-if="chat">
        <p>{{ chat.user1_id == auth.user.id ? chat.user2.email : chat.user1.email }}</p>
        <hr>
        <div v-for="message in chat.messages">
            <div v-if="message.author_id == auth.user.id" style="color: blue;">YOU: {{ message }}</div>
            <div v-if="message.author_id != auth.user.id">{{ message }}</div>
        </div>
        <hr>
        <input type="text" v-model="message" placeholder="message">
        <button v-on:click="send_message">Send</button>
    </div>

</template>


<script setup>
//imports
import Header from '@/components/Header.vue'
import api from '@/api/api'

import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRoute, useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()


//data
let chat_id = route.params.id
let chat = ref("")

let message = ref("")

//functions
onMounted(async () => {
    const res = await api.get(`/chats/${chat_id}`)
    chat.value = res.data
})

async function send_message() {
    let form = new FormData()
    form.append("text", message.value)
    const res = await api.post(`/chats/${chat_id}/messages`, form)
    chat.value.messages.push(res.data)
    message.value = ""
}

</script>

<style scoped></style>
