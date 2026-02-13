<template>
  <Header />

  <main class="page">
    <section class="card">
      <header class="card__head">
        <h1 class="title">Create post</h1>
        <p class="subtitle">Add a title and an optional image/file, then publish.</p>
      </header>

      <div class="form">
        <label class="field">
          <span class="field__label">Post title</span>
          <input
            class="input"
            type="text"
            v-model="post_title"
            placeholder="e.g. My first forged blade"
            autocomplete="off"
          />
        </label>

        <label class="field">
          <span class="field__label">Attachment (optional)</span>

          <div class="file">
            <input class="file__input" type="file" @change="onFileChange" />
            <div class="file__ui">
              <span class="file__badge">Choose file</span>
              <span class="file__name">
                {{ fileName || "No file selected" }}
              </span>
            </div>
          </div>

          <p class="hint">Images look best. Any file type is allowed if your backend supports it.</p>
        </label>

        <div class="actions">
          <button class="btn btn--primary" type="button" @click="submit" :disabled="isSubmitting">
            {{ isSubmitting ? "Publishing…" : "Publish" }}
          </button>

          <button class="btn btn--ghost" type="button" @click="router.push('/posts')" :disabled="isSubmitting">
            Cancel
          </button>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import Header from '@/components/Header.vue'
import api from '@/api/api'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const post_title = ref('')
const file = ref(null)
const isSubmitting = ref(false)

const fileName = computed(() => file.value?.name || '')

function onFileChange(e) {
  file.value = e.target.files?.[0] ?? null
}

async function submit() {
  if (!post_title.value.trim()) return

  try {
    isSubmitting.value = true

    const form = new FormData()
    form.append('title', post_title.value.trim())
    if (file.value) form.append('file', file.value)

    await api.post('/posts', form, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })

    router.push('/posts')
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
/* Page shell matches the header style language */
.page {
  min-height: calc(100vh - 64px);
  padding: 28px 20px;
  display: grid;
  place-items: start center;

  /* subtle background */
  background:
    radial-gradient(900px 400px at 20% 0%, rgba(255, 127, 80, 0.10), transparent 60%),
    radial-gradient(700px 360px at 90% 10%, rgba(139, 92, 246, 0.10), transparent 55%),
    #0b0b0f;
}

/* Card */
.card {
  width: min(720px, 100%);
  border-radius: 22px;
  padding: 18px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

.card__head {
  padding: 8px 8px 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  margin-bottom: 14px;
}

.title {
  margin: 0;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: 0.2px;
  color: rgba(255, 255, 255, 0.92);
}

.subtitle {
  margin: 8px 0 0;
  color: rgba(255, 255, 255, 0.68);
  font-size: 14px;
  line-height: 1.4;
}

/* Form */
.form {
  display: grid;
  gap: 14px;
  padding: 6px 8px 10px;
}

.field {
  display: grid;
  gap: 8px;
}

.field__label {
  font-size: 13px;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.78);
}

/* Inputs */
.input {
  width: 100%;
  padding: 12px 12px;
  border-radius: 14px;

  color: rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.10);

  outline: none;
  transition: box-shadow 180ms ease, border-color 180ms ease, background 180ms ease;
}

.input::placeholder {
  color: rgba(255, 255, 255, 0.45);
}

.input:focus {
  border-color: rgba(255, 127, 80, 0.35);
  box-shadow: 0 0 0 4px rgba(255, 127, 80, 0.14);
  background: rgba(255, 255, 255, 0.04);
}

/* File input (custom UI) */
.file {
  position: relative;
}

.file__input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
  width: 100%;
  height: 100%;
}

.file__ui {
  display: flex;
  align-items: center;
  gap: 12px;

  padding: 12px 12px;
  border-radius: 14px;

  background: rgba(255, 255, 255, 0.03);
  border: 1px dashed rgba(255, 255, 255, 0.18);

  transition: box-shadow 180ms ease, border-color 180ms ease, background 180ms ease;
}

.file:hover .file__ui {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.26);
}

.file:focus-within .file__ui {
  border-color: rgba(255, 127, 80, 0.35);
  box-shadow: 0 0 0 4px rgba(255, 127, 80, 0.14);
}

.file__badge {
  flex: 0 0 auto;
  padding: 8px 10px;
  border-radius: 12px;
  font-weight: 800;
  font-size: 12px;

  color: rgba(255, 255, 255, 0.92);
  background: linear-gradient(135deg, rgba(255, 127, 80, 0.9), rgba(139, 92, 246, 0.85));
}

.file__name {
  color: rgba(255, 255, 255, 0.72);
  font-size: 13px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hint {
  margin: 0;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.55);
}

/* Actions */
.actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
  padding-top: 6px;
}

/* Buttons (same language as Header) */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  padding: 10px 14px;
  border-radius: 14px;

  font-weight: 800;
  font-size: 14px;

  border: 1px solid transparent;
  cursor: pointer;
  user-select: none;

  transition: transform 180ms ease, background 180ms ease, box-shadow 180ms ease, opacity 180ms ease;
}

.btn:active {
  transform: translateY(1px);
}

.btn:disabled {
  opacity: 0.55;
  cursor: not-allowed;
  transform: none;
}

.btn--primary {
  color: #fff;
  background: linear-gradient(135deg, #ff7f50, #8b5cf6);
  box-shadow: 0 12px 26px rgba(255, 127, 80, 0.18);
}

.btn--primary:hover {
  box-shadow: 0 16px 34px rgba(255, 127, 80, 0.24);
}

.btn--ghost {
  color: rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.10);
}

.btn--ghost:hover {
  background: rgba(255, 255, 255, 0.07);
}

@media (max-width: 520px) {
  .actions {
    flex-direction: column;
  }
  .btn {
    width: 100%;
  }
}
</style>
