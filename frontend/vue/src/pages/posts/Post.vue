<template>
    <Header />
    <h1>Post</h1>

    <div v-if="post">
        <p>post title: {{ post.title }}</p>
        <p>user name: {{ post.author?.name }}</p>
        <button type="button" v-on:click="delete_post()">Delete</button>
    </div>

</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const post = ref(null);
const post_id = route.params.id; 

onMounted(async () => {
    const res = await api.get(`/posts/${post_id}`);
    post.value = res.data;
})

async function delete_post() {
    const res = await api.delete(`/posts/${post_id}`);
    router.push("/posts")
}

</script>
