<template>
    <div class="form-container">
        <h1>You can create short url as a guest or login to have access to your urls.</h1>
        <form @submit.prevent="handleLogin" class="auth-form">
            <input v-model="form.username" placeholder="Username" required>
            <input v-model="form.password" type="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <h2>Create short url</h2>
        <form @submit.prevent="handleCreateShortUrl" class="input-form">
            <input v-model="shortenedURLForm.original_url" placeholder="Original URL" required>
            <button type="submit">Create Short URL</button>
        </form>
        <h3>Don't have an account?</h3>
        <button @click="handleRegisterRedirect" class="register-redirect-button">Register</button>
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
        console.error(error)
    }
}

const handleLogin = async () => {
    try {
        const response = await api.post('login/', form.value)
        localStorage.setItem('token', response.data.token)
        router.push('/dashboard')
    } catch (error) {
        alert('Login failed!')
    }
}
</script>