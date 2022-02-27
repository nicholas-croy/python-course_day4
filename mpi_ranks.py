# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:08:16 2022

@author: niccr151
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hello world from process ",rank)