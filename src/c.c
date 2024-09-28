#include <stdio.h>

int main() {
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; // Initial array
    int size = 10;
    int i, pos, element;

    // Print the original array
    printf("Original array: ");
    for(i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Insert an element
    printf("Enter element to insert: ");
    scanf("%d", &element);
    printf("Enter position to insert (0-9): ");
    scanf("%d", &pos);

    // Shift elements to the right
    for(i = size; i > pos; i--) {
        arr[i] = arr[i-1];
    }
    arr[pos] = element;
    size++;

    // Print the array after insertion
    printf("Array after insertion: ");
    for(i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Delete an element
    printf("Enter position to delete (0-9): ");
    scanf("%d", &pos);

    // Shift elements to the left
    for(i = pos; i < size-1; i++) {
        arr[i] = arr[i+1];
    }
    size--;

    // Print the array after deletion
    printf("Array after deletion: ");
    for(i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}