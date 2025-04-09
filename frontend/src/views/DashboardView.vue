<template>
    <div class="dashboard-container">
        <h1>Welcome to your dashboard</h1>
        <ul>
            <li v-for="url in urls" :key="url.id" class="url-item">
                <a :href="url.original_url">{{ url.original_url }}</a>
                <p>{{ url.short_code }}</p>
            </li>               
        </ul>
        <button @click="handleLogout" class="logout-button">Logout</button> 
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/auth.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const urls = ref([])

const handleLogout = async () => {
    try {
        localStorage.removeItem('token')
        router.push('/login')
    } catch (error) {
        console.error('Error logging out:', error)
    }
}

onMounted(fetchUrls)

async function fetchUrls() {
    try {
        const response = await api.get('/shorten/list/')
        urls.value = response.data
    } catch (error) {
        console.error('Error fetching URLs:', error)
    }
}
</script>