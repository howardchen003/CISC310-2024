import random

def fifo(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    
    for page in page_reference_string:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
    
    return page_faults

def lru(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    counter = 0
    
    for page in page_reference_string:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                min_counter = min(counter for counter, frame in enumerate(frames))
                frames[min_counter] = page
            page_faults += 1
        counter += 1
    
    return page_faults

def optimal(page_reference_string, num_frames):
    page_faults = 0
    frames = []
    
    for page in page_reference_string:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                future_pages = page_reference_string[page_reference_string.index(page):]
                max_distance = max(future_pages.index(frame) if frame in future_pages else len(future_pages) for frame in frames)
                frames[frames.index(page_reference_string[max_distance])] = page
            page_faults += 1
    
    return page_faults

# Generate random page-reference string
random.seed(0)
random_page_reference_string = [random.randint(0, 9) for _ in range(20)]

# Given page-reference strings
page_reference_string1 = [0, 7, 0, 1, 2, 0, 8, 9, 0, 3, 0, 4, 5, 6, 7, 0, 8, 9, 1, 2]
page_reference_string2 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

# Compute page faults for each algorithm and number of frames
for num_frames in range(1, 8):
    print(f"Number of frames: {num_frames}")
    print(f"FIFO page faults (random): {fifo(random_page_reference_string, num_frames)}")
    print(f"FIFO page faults (given): {fifo(page_reference_string1, num_frames)}")
    print(f"FIFO page faults (given): {fifo(page_reference_string2, num_frames)}")
    print(f"LRU page faults (random): {lru(random_page_reference_string, num_frames)}")
    print(f"LRU page faults (given): {lru(page_reference_string1, num_frames)}")
    print(f"LRU page faults (given): {lru(page_reference_string2, num_frames)}")
    print(f"Optimal page faults (random): {optimal(random_page_reference_string, num_frames)}")
    print(f"Optimal page faults (given): {optimal(page_reference_string1, num_frames)}")
    print(f"Optimal page faults (given): {optimal(page_reference_string2, num_frames)}")
    print()
    print("--------------------")