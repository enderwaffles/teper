
<template>
    <h1>{{ title }}</h1>
    <h1>{{ name1 }}</h1>
    <input type="text" placeholder="name" v-model="name">
    <button v-on:click="click()">Click</button>
</template>

<script setup>
import { ref } from 'vue';

defineProps ({
    title: String,
})

const emit = defineEmits(["submit"])

const name1 = ref("")
const name = ref("")
function click() {
    console.log("clicked")
    name1.value = name.value; 
    emit("submit", name1.value)
}

</script>

