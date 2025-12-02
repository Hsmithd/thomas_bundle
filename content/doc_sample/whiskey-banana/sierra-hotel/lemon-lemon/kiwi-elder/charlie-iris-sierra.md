# Play: Charlie - setup

- hosts: db
  become: true
  vars:
    app_name: "charlie_app"
    retry_count: 5

  tasks:
    - name: Ensure whiskey-task-1 is present
      ansible.builtin.file:
        path: /opt/charlie/whiskey-task-1
        state: directory

    - name: Template whiskey-task-1 config
      ansible.builtin.template:
        src: templates/whiskey-task-1.j2
        dest: /etc/charlie/whiskey-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure romeo-task-2 is present
      ansible.builtin.file:
        path: /opt/charlie/romeo-task-2
        state: directory

    - name: Template romeo-task-2 config
      ansible.builtin.template:
        src: templates/romeo-task-2.j2
        dest: /etc/charlie/romeo-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure jasmine-task-3 is present
      ansible.builtin.file:
        path: /opt/charlie/jasmine-task-3
        state: directory

    - name: Template jasmine-task-3 config
      ansible.builtin.template:
        src: templates/jasmine-task-3.j2
        dest: /etc/charlie/jasmine-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure foxtrot-task-4 is present
      ansible.builtin.file:
        path: /opt/charlie/foxtrot-task-4
        state: directory

    - name: Template foxtrot-task-4 config
      ansible.builtin.template:
        src: templates/foxtrot-task-4.j2
        dest: /etc/charlie/foxtrot-task-4.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart charlie service
      ansible.builtin.service:
        name: charlie
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:43Z
