# Play: Banana - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "banana_app"
    retry_count: 1

  tasks:
    - name: Ensure grape-task-1 is present
      ansible.builtin.file:
        path: /opt/banana/grape-task-1
        state: directory

    - name: Template grape-task-1 config
      ansible.builtin.template:
        src: templates/grape-task-1.j2
        dest: /etc/banana/grape-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure iris-task-2 is present
      ansible.builtin.file:
        path: /opt/banana/iris-task-2
        state: directory

    - name: Template iris-task-2 config
      ansible.builtin.template:
        src: templates/iris-task-2.j2
        dest: /etc/banana/iris-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure echo-task-3 is present
      ansible.builtin.file:
        path: /opt/banana/echo-task-3
        state: directory

    - name: Template echo-task-3 config
      ansible.builtin.template:
        src: templates/echo-task-3.j2
        dest: /etc/banana/echo-task-3.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure romeo-task-4 is present
      ansible.builtin.file:
        path: /opt/banana/romeo-task-4
        state: directory

    - name: Template romeo-task-4 config
      ansible.builtin.template:
        src: templates/romeo-task-4.j2
        dest: /etc/banana/romeo-task-4.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart banana service
      ansible.builtin.service:
        name: banana
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
