import numpy as np
import heapq

def testPositionInImageBounds(y: int, x: int, dims: tuple):
    # TODO: implement/finish this function this function tests if a x,y coordinate position is inside the bounds of
    #  the image according to image dimensions dims (put differently, if it is a valid 2D index)
    """
        Check if a given (x, y) coordinate is within the bounds of an image.

        Args:
            y (int): The y-coordinate.
            x (int): The x-coordinate.
            dims (tuple): A tuple (height, width) representing the image dimensions.

        Returns:
            bool: True if the coordinate is within bounds, False otherwise.
        """
    height, width = dims
    return 0 <= x < width and 0 <= y < height


def damPixelTest(labelMap: np.array, y: int, x: int):
    # TODO: implement/finish this function this function needs true if the pixel at position [y,x] is a dam pixel see
    #  page 33 on the slides - if at least one neighboring pixel fulfils the condition from the slides return True,
    #  otherwise False
    """
        Check if a pixel at position [y, x] in the label map is a "dam pixel"
        based on a condition satisfied by at least one neighboring pixel.

        Args:
            labelMap (np.array): A NumPy array representing the label map.
            y (int): The y-coordinate of the pixel.
            x (int): The x-coordinate of the pixel.

        Returns:
            bool: True if the pixel is a "dam pixel," False otherwise.
        """
    # Define the condition for a neighboring pixel to satisfy
    condition = lambda label: label == 1  # Replace with your specific condition

    # Check the pixel's neighborhood (8-connected neighbors)
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if 0 <= y + dy < labelMap.shape[0] and 0 <= x + dx < labelMap.shape[1]:
                neighbor_label = labelMap[y + dy, x + dx]
                if condition(neighbor_label):
                    return True

    # If no neighboring pixel satisfies the condition, return False
    return False


def buildListOfNeighborPixels(gradMag: np.array, labelMap: np.array, usageMap: np.array, label: int, y: int, x: int):
    # TODO: implement/finish this function this list should at the end of this function have an entry for all
    #  neighboring pixels (that have not yet an label assigned and have not been previously added to the priority queue)

    # TODO1: loop over all neighbor pixels of current postion [y,x] and add pixels to list listNewPixels in case they
    # have no label assigned yet (info can be found in labelMap) and have not been previously added to the priority
    # queue (use usageMap for this)
    #
    # TODO2: for every pixel store a list of properties as one entry in listNewPixels (
    # list in a list)
    #
    # TODO3: the list of properties should contain label, y-pos, x-pos and the gradient magnitude
    # value at this position
    #
    # TODO4: mark those pixels added in the usageMap
    listNewPixels = []

    # Define the coordinates of neighboring pixels
    neighbors = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]

    for ny, nx in neighbors:
        # Check if the neighboring pixel is within the image boundaries
        if 0 <= ny < gradMag.shape[0] and 0 <= nx < gradMag.shape[1]:
            # Check if the neighboring pixel has no label assigned and hasn't been added to the priority queue
            if labelMap[ny, nx] == 0 and usageMap[ny, nx] == 0:
                # Store properties (label, y-pos, x-pos, gradient magnitude) in a list
                properties = [label, ny, nx, gradMag[ny, nx]]
                listNewPixels.append(properties)

                # Mark the pixel as added in the usageMap
                usageMap[ny, nx] = 1

    return listNewPixels






def computeWatershedSegmentation(gradMag: np.array, seedMap: np.array):
    # TODO: implement/finish this function
    #  TODO1: initialize labelMap (point 2 from slide #31) - make sure that you
    #  can store -1 in this map (be careful about the data type)

    # TODO2: initialize usageMap

    # TODO3: create initial processing list (priority queue)
    # processingList = []  # also point 2 from slide #31

    # TODO4: for every seed point in seedMap add new entry in processingList (initial positions for watershed
    # flooding process): for every initial seed pixel store a list of properties as one entry in processingList (so
    # one entry is a list inside the processingList (list in list)) the list of properties should contain label (use
    # a new label for every new seed point, first should get label 1, second should get label 2, and so on...),
    # y-pos, x-pos and the gradient magnitude value at this position

    # the main loop will then check if there is at least one remaining entry in the processingList (point 4 from
    # slide #31 and #32)...
    # while len(processingList) > 0:
    # at every loop iteration, print out the number of entries in processingList - this way, we know,
    # how many pixels at least need to be processed before the algorithm can terminate (of course, this number
    # will increase as long as neighboring pixels get added)
    # print(len(processingList))

    # TODO5: process the first element of processingList (since the list should be sorted, always picking the
    # first element resembles the behaviour of a priority queue)
    # 		obtain y-,x- position, label and gradient magnitude value from the first entry of the list

    # TODO6: set label of current pixel in labelmap before doing the dam pixel test (since the test compares the
    # label with the neighboring pixel's label)

    # TODO7: mark current pixel as pixel, that was added to priority queue (use usageMap for this)

    # TODO8: next thing to do is to perform the dam pixel test (use function damPixelTest here), if pixel is found to
    # be a dam pixel mark the pixel in the labelMap with label -1

    # TODO9: remove the first element of the processingList (remove the current pixel that has just been processed)

    # TODO10: build the list of neighbor pixels which are not part of the processingList already (use function
    # buildListOfNeighborPixels here)

    # TODO11: add the new neighbor pixels to the processing queue

    # TODO12: then sort the list according to its gradient magnitude value



    # Initialize labelMap with -1, usageMap with 0
    labelMap = np.full_like(gradMag, -1, dtype=np.int32)
    usageMap = np.zeros_like(gradMag, dtype=np.uint8)

    # Initialize processingList as a priority queue
    processingList = []

    # Define neighboring coordinates [(y, x)]
    neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    current_label = 0  # Initialize the label counter

    # Iterate over seed points in seedMap
    for y_seed, x_seed in np.transpose(np.where(seedMap > 0)):
        current_label += 1
        properties = [current_label, y_seed, x_seed, gradMag[y_seed, x_seed]]
        heapq.heappush(processingList, properties)

    while len(processingList) > 0:
        print(len(processingList))  # Print the number of remaining entries

        # Process the first element in processingList
        current_label, y, x, _ = heapq.heappop(processingList)

        # Set the label in labelMap
        labelMap[y, x] = current_label

        # Mark as added to the priority queue
        usageMap[y, x] = 1

        # Perform the dam pixel test
        if damPixelTest(labelMap, y, x):
            labelMap[y, x] = -1

        # Build the list of neighbor pixels
        neighborPixels = buildListOfNeighborPixels(gradMag, labelMap, usageMap, current_label, y, x)

        # Add new neighbor pixels to the processing queue
        for neighbor in neighborPixels:
            heapq.heappush(processingList, neighbor)

        # Sort the processingList based on gradient magnitude
        processingList.sort(key=lambda p: p[3])

    return labelMap




