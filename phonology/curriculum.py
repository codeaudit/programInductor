import os
import sys

def numberOfCPUs():
    import multiprocessing
    return multiprocessing.cpu_count()


def flushEverything():
    sys.stdout.flush()
    sys.stderr.flush()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Curriculum solving of phonology problems. Calls out to UG.py and driver.py")
    parser.add_argument("startingIndex",
                        type=int,
                        help="Which problem to start out solving. 0-indexed")
    parser.add_argument("endingIndex",
                        type=int)
    parser.add_argument("ug",
                        choices=["empirical","ground","none"],
                        help="What kind of universal grammars to use. empirical: estimate from solutions found to previous problems. ground: estimate using textbook solutions. none: do not use universal grammar.")
    parser.add_argument("--CPUs",
                        type=int,
                        default=None)
    parser.add_argument("--timeout",
                        type=float,
                        default=None)
    parser.add_argument("--serial",
                        default=False,
                        action="store_true")
    
    arguments = parser.parse_args()
    def universal(j):
        if arguments.ug == "none":
            u = ""
        elif arguments.ug == "empirical":
            u = "--universal universalGrammars/empirical_%d.p"%j
        elif arguments.ug == "ground":
            u = "--universal universalGrammars/groundTruth_%d.p"%j
        else: assert False
        return u

    if arguments.ug == "ground":
        pickleDirectory = " --pickleDirectory frontierPickles/groundUniversal/ "
    elif arguments.ug == "none":
        pickleDirectory = " --pickleDirectory frontierPickles/noUniversal/ "
    elif arguments.ug == "empiricalUniversal":
        pickleDirectory = " --pickleDirectory frontierPickles/empiricalUniversal/ "
    else: assert False

    if arguments.timeout is None: timeout = ""
    else: timeout = " --timeout %f"%arguments.timeout

    CPUs = arguments.CPUs or numberOfCPUs()
    print("Using %d CPUs"%CPUs)

    os.system("python command_server.py %d &"%CPUs)

    if arguments.ug == "ground":
        print "Precomputing ground-truth universal grammars..."
        for j in xrange(arguments.startingIndex, arguments.endingIndex+1):
            os.system("pypy UG.py fromGroundTruth --CPUs %d --problems %d --export universalGrammars/groundTruth_%d.p"%(CPUs, j, j))

    if arguments.ug in ["ground","none"] and not arguments.serial:
        print "Launching all jobs in parallel!"
        import subprocess
        processes = [subprocess.Popen("python driver.py %d incremental --cores %d --top 100 %s %s %s" %
                                      (j, CPUs, pickleDirectory, universal(j), timeout),
                                      shell=True)
                     for j in xrange(arguments.startingIndex, arguments.endingIndex+1)]
        for p in processes:
            p.wait()

    else:
        for j in xrange(arguments.startingIndex, arguments.endingIndex+1):
            os.system("rm -rf ~/.sketch/tmp/*")
            os.system("rm -rf /scratch/ellisk/*")
            print("Solving problem %d"%j)
            command = "python driver.py %d incremental --cores %d --top 100 %s %s %s"%(j,CPUs,
                                                                                      universal(j),
                                                                                      pickleDirectory,
                                                                                      timeout)
            print
            print "\tCURRICULUM: Solving problem %d by issuing the command:"%j
            print "\t\t",command
            flushEverything()
            os.system(command)

            if arguments.ug == "empiricalUniversal":
                command = "pypy UG.py fromFrontiers --CPUs %d --problems %d --export universalGrammars/empirical_%d.p"%(CPUs, j, j)
                print
                print "Re- estimating universal grammar by executing:"
                print command
                os.system(command)


