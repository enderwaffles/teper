<template>
    <Header />

    <div>
        <h1>Chat</h1>
    </div>

    <div v-if="chat">
        
        <p>{{ chat.user1_id == auth.user.id ? chat.user2.email : chat.user1.email }}</p>
        <!-- <img :src="api.defaults.baseURL + chat.user1.avatar_url" alt="" style="width: 60px;"> -->
        <img :src="api.defaults.baseURL + (chat.user1_id == auth.user.id ? chat.user2.avatar_url : chat.user1.avatar_url)"
            alt="" style="width: 60px;">
        <hr>

        <div v-for="message in chat.messages">
            <div v-if="message.author_id == auth.user.id" style="color: blue;">
                <p>YOU: {{ message.text }}</p>
                <button v-on:click="delete_message(message.id)">Delete</button>

                <div v-if="message.uploads.length">
                    <div v-for="upload in message.uploads" :key="upload.id">
                        <img :src="api.defaults.baseURL + upload.upload_url" style="width:200px;">
                    </div>
                </div>

            </div>
            <div v-if="message.author_id != auth.user.id">
                <p>{{ message.text }}</p>
                <div v-if="message.uploads.length">
                    <div v-for="upload in message.uploads" :key="upload.id">
                        <img :src="api.defaults.baseURL + upload.upload_url" style="width:200px;">
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <input type="text" v-model="message" placeholder="message">
        <input type="file" multiple v-on:change="onFileChange">
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
let files = ref([])

let message = ref("")

//functions
onMounted(async () => {
    const res = await api.get(`/chats/${chat_id}`)
    chat.value = res.data
})

function onFileChange(e) {
    files.value = Array.from(e.target.files)
}

async function send_message() {

    let form = new FormData()
    form.append("text", message.value)

    files.value.forEach(file => {
        form.append("files", file)
    })

    await api.post(`/chats/${chat_id}/messages`, form)
    // chat.value.messages.push(res.data)
    message.value = ""
    files.value = []

    // заново подгружаем чат
    const res = await api.get(`/chats/${chat_id}`)
    chat.value = res.data

}

async function delete_message(message_id) {
    const res = await api.delete(`chats/messages/${message_id}`)
    chat.value.messages = chat.value.messages.filter(m => m.id !== message_id)
}

</script>

<style scoped></style>
