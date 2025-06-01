## 🗝️ Challenge: **Kaz Brekker’s Vault**

**Author:** Aman
**Difficulty:** Easy-Medium
**Flag:** `flag{no_lock_unpickable}`
**Description:**

> *“No mourners. No funerals.”*
> *In Ketterdam, alliances are forged not in ink, but in blood and broken promises.*
>
> Can you answer the one question that unlocks Kaz Brekker’s most secure vault?

---

### 🧠 Overview:

This challenge combines web inspection and YARA-based file analysis. You’re tasked with submitting a file that proves you understand what’s *essential for a true alliance*. If your file contains the correct phrase, the gatekeeper grants access to the vault—and your reward: the flag.

---

### 🕵️‍♀️ Challenge Flow:

#### 🔍 Step 1: Landing Page & Theme

Opening the challenge reveals a slick, thematic interface:

* Sidebar options with fun decoy buttons
* A central prompt to upload a file
* An elite "YARA inspection" awaits...

Some buttons may give fun alerts like:

```
🤔 What is essential for a true alliance?
```

That’s your **first major clue**.

---

#### 🧾 Step 2: File Upload Mechanics

Using browser dev tools or source inspection, you confirm that:

* Only `.txt` files are allowed.
* The server uses a **YARA rule** to scan uploaded files.

The rule looks for a **specific string**:

```yara
$secret_access_text = "Trust" ascii wide nocase
```

This means your file must contain the word:

```
Trust
```

(case-insensitive, wide string supported)

✅ **Correct input**: Create a file named `answer.txt` with this content:

```
Trust
```

---

#### 🔓 Step 3: Bypass the Vault

Once you upload the valid file, the message changes to:

```
Access Granted!
🎉 Success! Download your flag 🚩
```

A download link becomes available to grab the flag.

Visiting `/flag` gives you:

```
flag{no_lock_unpickable}
```

---

### 🏁 Final Flag:

```
flag{no_lock_unpickable}
```

---

> *In the words of the Dregs: “No mourners. No funerals.”*
> But the clever always leave with what they came for.
