# Play: Grape - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "grape_app"
    retry_count: 2

  tasks:
    - name: Ensure juliet-task-1 is present
      ansible.builtin.file:
        path: /opt/grape/juliet-task-1
        state: directory

    - name: Template juliet-task-1 config
      ansible.builtin.template:
        src: templates/juliet-task-1.j2
        dest: /etc/grape/juliet-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure victor-task-2 is present
      ansible.builtin.file:
        path: /opt/grape/victor-task-2
        state: directory

    - name: Template victor-task-2 config
      ansible.builtin.template:
        src: templates/victor-task-2.j2
        dest: /etc/grape/victor-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure romeo-task-3 is present
      ansible.builtin.file:
        path: /opt/grape/romeo-task-3
        state: directory

    - name: Template romeo-task-3 config
      ansible.builtin.template:
        src: templates/romeo-task-3.j2
        dest: /etc/grape/romeo-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart grape service
      ansible.builtin.service:
        name: grape
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z
