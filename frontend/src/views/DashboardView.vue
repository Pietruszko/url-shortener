<template>
    <div class="dashboard-container">
        <h1>Welcome to your dashboard</h1>
        <ul>
            <li v-for="url in urls" :key="url.id" class="url-item">
                <a :href="url.original_url">{{ url.original_url }}</a>
                <p>{{ url.short_code }}</p>
            </li>               
        </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '@/auth.js'
import { useRouter } from 'vue-router'

const router = useRouter()
const urls = ref([])

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