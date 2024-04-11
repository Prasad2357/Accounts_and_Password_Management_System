#include <stdio.h>
#include <string.h>

void encrypt(char *message, int key) {
    int length = strlen(message);
    for (int k = 0; k < key; k++) {
        for (int i = 0; i < length; i++) {
            message[i] = (message[i] + 1) % 128;
        }
    }
}

void decrypt(char *message, int key) {
    int length = strlen(message);
    for (int k = 0; k < key; k++) {
        for (int i = 0; i < length; i++) {
            message[i] = (message[i] - 1 + 128) % 128;
        }
    }
}

int main() {
    char message[1000];
    int key;

    printf("Enter a string to encrypt: ");
    fgets(message, sizeof(message), stdin);

    printf("Enter encryption key (an integer): ");
    scanf("%d", &key);

    encrypt(message, key);
    printf("Encrypted message: %s\n", message);

    decrypt(message, key);
    printf("Decrypted message: %s\n", message);

    return 0;
}

