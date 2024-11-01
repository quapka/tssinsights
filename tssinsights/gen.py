#!/usr/bin/env python3

import sys
import time

import subprocess as sp

import matplotlib.pyplot as plt


def generate_thresh_policy(thresh, n):
    parties = ", ".join(f"pk(a{ind})" for ind in range(n))
    policy = f"thresh({thresh}, {parties})"
    return policy

def generate_or_policy(n):
    return gen_alg_policy("or", n)

def generate_and_policy(n):
    return gen_alg_policy("and", n)

def gen_alg_policy(operator, n):
    policy = f"pk(a{n})"
    for ind in range(n - 1, 0, -1):
        policy = f"{operator}(pk(a{ind}), {policy})"
    return policy

def get_script_size(policy):
    size = int(sp.check_output(["./miniscript"], input=policy.encode()).decode().strip())
    return size

def plot_thresh_or_and_policies(max_size):
    th_1_sizes = []
    th_n_sizes = []
    or_sizes = []
    and_sizes = []
    for n in range(1, max_size):
        th_1_policy = generate_thresh_policy(1, n)
        th_n_policy = generate_thresh_policy(n, n)
        or_policy = generate_or_policy(n)
        and_policy = generate_and_policy(n)

        # start = time.time()
        th_1_sizes.append(get_script_size(th_1_policy))
        th_n_sizes.append(get_script_size(th_n_policy))
        or_sizes.append(get_script_size(or_policy))
        and_sizes.append(get_script_size(and_policy))
        # duration = time.time() - start
        # print(f"{duration:.03}:{n:02}")
        # print(f"{n:02}:{duration:.03}")

    plt.plot(th_1_sizes, label="Threshold 1-n")
    plt.plot(th_n_sizes, label="Threshold n-n")
    plt.plot(or_sizes, label="OR ~ 1-n")
    plt.plot(and_sizes, label="AND ~ n-n")
    plt.legend()
    # plt.ylabel('some numbers')
    plt.show()

def compare_time_to_generate_threshold_policies(max_size=10):

    th_1_comp_time = []
    th_2_comp_time = []
    th_n_comp_time = []
    for n in range(2, max_size):
        # for t in range(1, n):

        th_1_policy = generate_thresh_policy(1, n)
        start = time.time()
        get_script_size(th_1_policy)
        duration = time.time() - start
        th_1_comp_time.append(duration * 100)

        th_2_policy = generate_thresh_policy(2, n)
        start = time.time()
        get_script_size(th_2_policy)
        duration = time.time() - start
        th_2_comp_time.append(duration * 100)

        th_n_policy = generate_thresh_policy(n, n)
        start = time.time()
        get_script_size(th_n_policy)
        duration = time.time() - start
        th_n_comp_time.append(duration * 100)

    fig, ax = plt.subplots()
    ax.plot(th_1_comp_time, label="Threshold 1-n")
    ax.plot(th_2_comp_time, label="Threshold 2-n")
    ax.plot(th_n_comp_time, label="Threshold n-n")
    ax.legend()

    ax.set(xlabel='group size', ylabel='Time (ms)',
           title='Time to compile threshold policy')
    ax.grid()

    fig.savefig("test.png")
    plt.show()

if __name__ == "__main__":

    compare_time_to_generate_threshold_policies(14)
