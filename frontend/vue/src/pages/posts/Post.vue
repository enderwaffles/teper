<template>
    <Header />
    <h1>Post</h1>

    <div v-if="post">
        <p>post title: {{ post.name }}</p>
        <p>user name: {{ post.author?.name }}</p>
    </div>

</template>

<script setup>
import Header from '@/components/Header.vue';
import api from '@/api/api';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute()

const post = ref(null);
const post_id = route.params.id; 

onMounted(async () => {
    const res = await api.get(`/posts/${post_id}`);
    post.value = res.data;
})

</script>
