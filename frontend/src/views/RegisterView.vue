<template>
    <div class="form-container">
        <h1>Register</h1>
        <form @submit.prevent="handleRegister" class="auth-form">
            <input v-model="form.username" placeholder="Username" required>
            <input v-model="form.password" type="password" placeholder="Password" required>
            <input v-model="form.confirmPassword" type="password" placeholder="Confirm Password" required>
            <button type="submit">Register</button>
        </form>
    </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import api from '@/auth.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const form = ref({
    username: '',
    password: '',
    confirmPassword: ''
})

onMounted(() => {
    if (localStorage.getItem('token')) {
        router.push('/dashboard')
    }
})

const handleRegister = async () => {
    try {
        const response = await api.post('register/', {
            username: form.value.username,
            password: form.value.password
        })
        router.push('/login')
    } catch (error) {
        alert('Registration failed!')
    }
}
</script>