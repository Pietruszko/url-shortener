<template>
    <div class="min-h-screen w-full bg-black p-8">
        <div class="bg-emerald-600 mx-auto w-160 p-4 rounded-2xl m-32">
            <h1 class="text-center text-2xl">You can create short url as a guest or login to have access to your urls.</h1>
            <form @submit.prevent="handleLogin">
                <input v-model="form.username" placeholder="Username" required class="border-2 mr-2 p-1">
                <input v-model="form.password" type="password" placeholder="Password" required class="border-2 p-1">
                <button type="submit" class="bg-emerald-400 rounded-3xl p-1 m-1 border-black border-2 hover:bg-emerald-800">Login</button>
            </form>
            <h2>Create short url</h2>
            <form @submit.prevent="handleCreateShortUrl" class="input-form">
                <input v-model="shortenedURLForm.original_url" placeholder="Original URL" required class="border-2 p-1">
                <button type="submit" class="bg-emerald-400 rounded-3xl p-1 m-1 border-black border-2 hover:bg-emerald-800">Create Short URL</button>
            </form>
            <h3>Don't have an account?</h3>
            <button @click="handleRegisterRedirect" class="bg-emerald-400 rounded-3xl p-1 m-1 border-black border-2 hover:bg-emerald-800">Register</button>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { ref } from 'vue'
import api from '@/auth.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
    username: '',
    password: ''
})
const shortenedURLForm = ref({
    original_url: ''
})

onMounted(() => {
    if (localStorage.getItem('token')) {
        router.push('/dashboard')
    }
})

const handleRegisterRedirect = () => {
    try {
        router.push('/register')
    } catch (error) {
        alert('Register failed!')
    }
}

const handleLogin = async () => {
    try {
        const response = await api.post('login/', form.value)
        localStorage.setItem('token', response.data.access)
        router.push('/dashboard')
    } catch (error) {
        alert('Login failed!')
    }
}

const handleCreateShortUrl = async () => {
    try {
        const response = await api.post('shorten/', shortenedURLForm.value)
        alert(`Your shortened URL is: 127.0.0.1:8000/${response.data.short_code}`)
    } catch (error) {
        alert('Failed to create short URL')
    }
}
</script>